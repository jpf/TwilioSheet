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

get '/' do
  'Hello world'
end
