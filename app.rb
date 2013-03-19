require 'sinatra'
require 'oauth'
require 'oauth/consumer'
require 'dotenv'

Dotenv.load
configure do
  enable :sessions
  set :session_secret, ENV['SESSION_SECRET']
end

before do
  @consumer ||= OAuth::Consumer.new(
    ENV['GOOGLE_CLIENT_ID'],
    ENV['GOOGLE_CLIENT_SECRET'],
    site: 'https://accounts.google.com/o/oauth2/auth'
  )
  @google_request_token = session[:google_request_token]
  @google_access_token = session[:google_access_token]
end

get '/' do
  if @google_access_token
    "You're logged in!"
  else
    redirect '/login/google'
  end
end

get '/login/google' do
  # require 'debugger'; debugger
  @google_request_token = @consumer.get_request_token
  session[:google_request_token] = @request_token.token
  session[:google_request_token_secret] = @request_token.secret
  redirect @google_request_token.authorize_url
end

get '/oauth2callback' do
  @google_access_token = @google_request_token.get_access_token oauth_verifier: params[:oauth_verifier]
  session[:google_access_token] = @google_access_token.token
  session[:google_access_token_secret] = @google_access_token.secret
  redirect '/'
end
