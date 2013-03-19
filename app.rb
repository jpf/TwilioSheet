require 'sinatra'
require 'oauth/consumer'
require 'dotenv'

Dotenv.load
configure do
  enable :sessions
  set :session_secret, ENV['SESSION_SECRET']
end

get '/' do
  "Hello World!"
end

get '/oauth2callback' do
  "Hello World!"
end
