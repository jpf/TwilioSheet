require 'sinatra'
require 'omniauth-google-oauth2'
require 'dotenv'
require 'google_drive'

Dotenv.load
configure do
  enable :sessions
  set :session_secret, ENV['SESSION_SECRET']
end

# FIXME: limit the scope to just what we need (probably userinfo.profile and spreadsheets)
use OmniAuth::Builder do
  provider :google_oauth2, ENV["GOOGLE_CLIENT_ID"], ENV["GOOGLE_CLIENT_SECRET"],
    scope: ["userinfo.email",
            "userinfo.profile",
            "https://docs.google.com/feeds/",
            "http://docs.googleusercontent.com/",
            "https://spreadsheets.google.com/feeds/"].join(',')
end

before do
  @google_auth = session[:google_auth]
end

get '/' do
  if @google_auth
    session[:google] = GoogleDrive.login_with_oauth @google_auth.credentials.token
  else
    redirect '/auth/google_oauth2'
  end
end

get '/create' do
  google = session[:google]
  spreadsheet = google.create_spreadsheet("TwilioSheet")
  spreadsheet_key = spreadsheet.key()
  auth_token = @google_auth.credentials.token
  url = "#{request.env['rack.url_scheme']}://#{request.env['HTTP_HOST']}/#{auth_token}/#{spreadsheet_key}"
  "Use this URL: #{url}"
end

get '/inspect' do
  content_type 'text/plain'
  @google_auth.inspect
end

get '/logout' do
  session[:google_auth] = nil
end

post '/sms/:auth_token/:spreadsheet_key' do
  google = GoogleDrive.login_with_oauth params[:auth_token]
  worksheet = google.spreadsheet_by_key(params[:spreadsheet_key]).worksheets[0]

  params.delete :spreadsheet_key
  params.delete :auth_token
  worksheet.list.push({'To' => params[:To], 'From' => params[:From], 'Body' => params[:Body]})
  worksheet.save
end

get '/auth/google_oauth2/callback' do
  session[:google_auth] = request.env['omniauth.auth']
  redirect '/'
end
