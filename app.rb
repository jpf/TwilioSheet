require 'sinatra'
require 'oauth/consumer'
require 'dotenv'
Dotenv.load

get '/' do
  "Hello World!"
end

get '/oauth2callback' do
  "Hello World!"
end
