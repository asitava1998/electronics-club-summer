import record_audio
import search
import trending
import weather
import mailtest
import mailtest2
import bingsearch
import chatterbotapitest
from chatterbotapi import ChatterBotFactory, ChatterBotType

counter=0
user=0

def listen():

	speech=record_audio.main(0)
	#counter+=1
	return speech

	'''if counter==999:
		user+=1
		counter=0
		if user==4:
			user=0
'''


def chat(speech):
    factory = ChatterBotFactory()

    bot1 = factory.create(ChatterBotType.CLEVERBOT)
    bot1session = bot1.create_session()

    bot2 = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
    bot2session = bot2.create_session()

    
    print 'yam> ' + bot1session.think(speech)
    
    while (1):

       r = record_audio.main(0);
       r= r.lower()

       if r=='bye bye':
       	break
       s = bot1session.think(r);
       print 'yam> ' + s


def do(speech):

	if speech.find("search twitter for")!=-1:
		speech=speech.replace("search twitter for",'')
		search.main(speech)
	elif speech.find("show twitter trend")!=-1:
		trending.main()
	elif speech.find("tell the weather")!=-1:
		weather.main()
	elif speech.find('show my e-mail')!=-1:
		mailtest.main()
	elif speech.find('send email')!=-1:
		mailtest2.main()
	elif speech.find('search bing for')!=-1:
		speech=speech.replace('search bing for','')
		bingsearch.main(speech)
	
	chat(speech)
		

def main():
	
	speech=listen()
	speech=speech.lower()
	print speech
	do(speech)

main()
