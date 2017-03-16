#!/usr/bin/python

import os
import record_audio
os.chdir('/home/pratyush/Downloads/Desktop')

#import modules
number = 50;
factory = ChatterBotFactory()
bot2 = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
bot2session = bot2.create_session()

   def main():
        factory = ChatterBotFactory()
        print 'hi'
        bot2 = factory.create(ChatterBotType.PANDORABOTS, 'b0dafd24ee35a477')
        bot2session = bot2.create_session()

        api = get_api()
        if not api:
            return
        try:
            status = api.received_messages(count=1)
        except tweetpony.APIError as err:
            print "Oh no! Your tweet could not be sent. Twitter returned error #%i and said: %s" % (err.code, err.description)
        else:
           message_id=status[0]['id']
           user_id=status[0]['sender_screen_name']
        status = api.received_messages(since_id=message_id)
        while(1):
            if status:
                message_id=status[0]['id']
                user_id=status[0]['sender_screen_name']
                s = status[0]['text']
                if s=='Take':
                
                    s='You can download the image from the link - '+take_image();
                else:
                    s = bot2session.think(s);
                api.send_message(screen_name=user_id,text=s)
            time.sleep(60)
            status=api.received_messages(since_id=message_id)           
            
   # if __name__ == "__main__":
    main()        
