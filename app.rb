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
    @session = GoogleDrive.login_with_oauth @google_auth.credentials.token
    @session.files.map(&:title).join(',')
  else
    redirect '/auth/google_oauth2'
  end
end

get '/inspect' do
  content_type 'text/plain'
  @google_auth.inspect
end

get '/logout' do
  session[:google_auth] = nil
end

get '/auth/google_oauth2/callback' do
  session[:google_auth] = request.env['omniauth.auth']
  redirect '/'
end
