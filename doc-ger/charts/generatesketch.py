
centerradius = 5
solradius = 5
anglefontsize = 20

import io, re, string, sys, math

def strip(line):
  for c in " ":
    line = string.replace(line, c, '')
  return line

f = open('../../chaospendel/network/data_pendulum', 'r');

maxpendlength = 0
radius = []
angles = []
coils = []

sys.stderr.write("loading file ...\n");

for line in f:
  if len(line) is 0: break;
  mo = re.search(u'([a-z\d]+)=([\d\.\-]+)', strip(line))
  if mo is None: continue
  if mo.group(1) == "l1":
    maxpendlength += float(mo.group(2))
  elif mo.group(1) == "l2b":
    maxpendlength += float(mo.group(2))
  else:
    mo2 = re.search(u'([a-z]+)(\d+)', mo.group(1));
    if mo2 is None: continue
    else:
      if mo2.group(1) == "solradius":
        radius.append(float(mo.group(2)))
      elif mo2.group(1) == "solangle":
        angles.append(float(mo.group(2)))
      elif mo2.group(1) == "solcoils":
        coils.append(float(mo.group(2)))

sys.stderr.write("maximum pendulum length: "+str(maxpendlength)+"\n");
sys.stderr.write("formatting svg ...\n");

print """<?xml version="1.0" ?>"""
print """<svg xmlns="http://www.w3.org/2000/svg">"""

imagewidth = 1000
scale = (imagewidth * (4.0/5.0) / 2) / maxpendlength

# center
print '<circle cx="'+str(imagewidth/2)+'" cy="'+str(imagewidth/2)+'" r="'+str(centerradius)+'" fill="black" />'
# coordinate axes
print '<line x1="'+str(imagewidth/2)+'" y1="'+str(imagewidth/2)+'" x2="'+str(imagewidth/2)+'" y2="'+str(imagewidth)+'" stroke="black" stroke-width="1" stroke-dasharray="5, 5" />'
print '<line x1="0" y1="'+str(imagewidth/2)+'" x2="'+str(imagewidth)+'" y2="'+str(imagewidth/2)+'" stroke="black" stroke-width="1" stroke-dasharray="5, 5" />'

# solenoids
index = 0
for (r, a, c) in zip(radius, angles, coils):
  xpos = math.sin(a / 360 * 2 * math.pi) * r * scale + imagewidth/2;
  ypos = math.cos(a / 360 * 2 * math.pi) * r * scale + imagewidth/2;
  # dashed line connecting solenoids with center
  print '<line x1="'+str(imagewidth/2)+'" y1="'+str(imagewidth/2)+'" x2="'+str(xpos)+'" y2="'+str(ypos)+'" stroke="grey" stroke-width="1" stroke-dasharray="2, 2" />'
  # colored circle
  if c > 10000: print '<circle cx="'+str(xpos)+'" cy="'+str(ypos)+'" r="'+str(solradius)+'" fill="darkgreen" />'
  else: print '<circle cx="'+str(xpos)+'" cy="'+str(ypos)+'" r="'+str(solradius)+'" fill="red" />'
  # text: index
  print '<text x="'+str(xpos+solradius)+'" y="'+str(ypos-anglefontsize)+'" fill="black" font-size="'+str(anglefontsize)+'">idx: S'+str(index)+'</text>'
  # text: radius
  print '<text x="'+str(xpos+solradius)+'" y="'+str(ypos)+'" fill="black" font-size="'+str(anglefontsize)+'">'+str(r)+'m</text>'
  # text: angle
  print '<text x="'+str(xpos+solradius)+'" y="'+str(ypos+anglefontsize)+'" fill="black" font-size="'+str(anglefontsize)+'">'+str(a)+'&#176;</text>'
  
  index += 1

print """</svg>"""
