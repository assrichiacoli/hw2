import re

isocitrate = 'MKTRTQQIEELQKEWTQPRWEGITRPYSAEDVVKLRGSVNPECTLAQLGAAKMWRLLHGE\
              SKKGYINSLGALTGGQALQQAKAGIEAVYLSGWQVAADANLAASMYPDQSLYPANSVPAV\
              VERINNTFRRADQIQWSAGIEPGDPRYVDYFLPIVADAEAGFGGVLNAFELMKAMIEAGA\
AAVHFEDQLASVKKCGHMGGKVLVPTQEAIQKLVAARLAADVTGVPTLLVARTDADAADL\
ITSDCDPYDSEFITGERTSEGFFRTHAGIEQAISRGLAYAPYADLVWCETSTPDLELARR\
FAQAIHAKYPGKLLAYNCSPSFNWQKNLDDKTIASFQQQLSDMGYKFQFITLAGIHSMWF\
NMFDLANAYAQGEGMKHYVEKVQQPEFAAAKDGYTFVSHQQEVGTGYFDKVTTIIQGGTS\
SVTALTGSTEESQF'

x = re.search(r'K[KR]CGH[LMQR]', isocitrate)
pos = x.start()
site = x.group()
z1 = isocitrate[pos-3:pos].lower()
z2 = isocitrate[pos+len(site):pos+len(site)+3].lower()
print('{} {} {}{} {}'.format('Isocitrate lyase (P9WKK7) contains its active site (PS00161)', 'starting from', pos, 'th position: ', z1+site+z2))
