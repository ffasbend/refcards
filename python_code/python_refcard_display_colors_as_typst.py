#!/usr/bin/python
#
# py-pygame-display-colors-htm.py
#
# Produces a table of all the pygame colours.
#
# This  program  is free software: you can redistribute it and/or  modify it
# under the terms of the GNU General Public License as published by the Free
# Software  Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This  program  is  distributed  in the hope that it will  be  useful,  but 
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public  License
# for more details.
#
# You  should  have received a copy of the GNU General Public License  along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# https://stackoverflow.com/questions/3121979
#
import sys
import pygame 
   

 
def _RGB (col):
  return '#%06X' %  ((col[0] * 256 + col[1]) * 256 +col[2]) # Ignores alpha
 
def get_basecolours(colours):
    base_colours = []
    for colour, value in colours:
        #print(colour[0:4])
        if not colour[-1].isdigit() and colour[0:4] != "grey" and colour[0:4] != "gray":
            base_colours.append(colour)
    return base_colours

_colour_names = list(pygame.colordict.THECOLORS.items())
_colour_names.sort(key=lambda name: name[0]) # Sort list by colour name
 
all_colours = dict((_colour_names))

base_colours = get_basecolours(_colour_names)
single_colours = [] # list of colours with no variants
multiple_colours = [] # list of colours with 5 variants: colour, colour1, ..., colour4
for colour in base_colours:
    if colour+"1" in all_colours:
        multiple_colours.append(colour)
    else:
        single_colours.append(colour)

# grey/gray colours
print()
print("--- grey / gray colors ---")
print()
print("[],", end="")
for i in range(20):
    print(f'[{i}],',end="")
print()
print("[grey0],")

for i in range(100):
    if i % 20 == 0 and i != 0:
        print()
        print(f"[grey{i}],")
    rgb = _RGB(all_colours["gray"+str(i)])
    del all_colours["grey"+str(i)] # remove from dict
    del all_colours["gray"+str(i)]
    print(f'[#rect(fill:rgb("{rgb}"))], ')

print()
print("--- color, color1, ... color4 (blocks of 5) ---")
print()

#print(multiple_colours)
#print(len(multiple_colours))

print("[], ", end="")
for i in range(5):
    print(f'[{i}], ', end="")
print()
for colour in multiple_colours:
    print(f'[{colour}],')
    rgb = _RGB(all_colours[colour])
    print(f'[#rect(fill:rgb("{rgb}"))], ')
    del all_colours[colour]
    for i in range(1, 5):
        rgb = _RGB(all_colours[colour+str(i)])
        print(f'[#rect(fill:rgb("{rgb}"))], ')
        del all_colours[colour+str(i)]

#print(single_colours)
#print(len(single_colours))
print()
print("--- remaining single colors ---")
print()
for colour in all_colours:
    print(f'[{colour}], ', end="")
    rgb = _RGB(all_colours[colour])
    print(f'[#rect(fill:rgb("{rgb}"))], ')
    #del all_colours[colour]



pygame.quit()
exit()

