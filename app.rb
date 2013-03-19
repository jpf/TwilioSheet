require 'sinatra'
require 'omniauth-google-oauth2'
require 'dotenv'

Dotenv.load
configure do
  enable :sessions
  set :session_secret, ENV['SESSION_SECRET']
end

use OmniAuth::Builder do
  provider :google_oauth2, ENV["GOOGLE_CLIENT_ID"], ENV["GOOGLE_CLIENT_SECRET"]
end

before do
  @google_auth = session[:google_auth]
end

get '/' do
  if @google_auth
    'Hello world'
  else
    redirect '/auth/google_oauth2'
  end
end

get '/auth/google_oauth2/callback' do
  session[:google_auth] = request.env['omniauth.auth']
  redirect '/'
end
