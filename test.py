import feedparser
d=feedparser.parse('https://www.e-distributie.com/ro-RO/_layouts/15/EnelRomania.RSS/Rss.aspx?Companii=Muntenia')
print (d['feed']['subtitle'])

