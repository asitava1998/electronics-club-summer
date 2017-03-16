from chatterbotapi import ChatterBotFactory, ChatterBotType
import record_audio

"""
    chatterbotapi
    Copyright (C) 2011 pierredavidbelanger@gmail.com

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""


def main(speech):
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