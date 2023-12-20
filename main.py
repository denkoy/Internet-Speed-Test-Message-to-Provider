from internet_speed_test import SpeedTest
from send_tweet import SendTweet

upload=input("Your minimal upload speed according to contract with internet provider: ")
download=input("Your minimal download speed according to contract with internet provider: ")

test_results=SpeedTest()
if test_results.up<upload and test_results.down<download:
    tweet_sender=SendTweet(test_results.up,test_results.down)