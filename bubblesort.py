"""
    Copyright 2021 by Sebastian Haacke

    bubblesort.py

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Dieses Programm ist Freie Software: Sie können es unter den Bedingungen
    der GNU General Public License, wie von der Free Software Foundation,
    Version 3 der Lizenz oder (nach Ihrer Wahl) jeder neueren
    veröffentlichten Version, weiter verteilen und/oder modifizieren.

    Dieses Programm wird in der Hoffnung bereitgestellt, dass es nützlich sein wird, jedoch
    OHNE JEDE GEWÄHR,; sogar ohne die implizite
    Gewähr der MARKTFÄHIGKEIT oder EIGNUNG FÜR EINEN BESTIMMTEN ZWECK.
    Siehe die GNU General Public License für weitere Einzelheiten.

    Sie sollten eine Kopie der GNU General Public License zusammen mit diesem
    Programm erhalten haben. Wenn nicht, siehe <https://www.gnu.org/licenses/>.
"""

# for a clean screen at the beginning.
import os

# for pause after sorting.
import time

from typing import List

# clear screen at beginning.
def clear_console():
    os.system('clear')

clear_console()

# the list - feel free to edit.
numbers = [7,3,5,4,6,9,1,2,0,8,23,65,75,44,81,29,66,24,102,294,3827,434]

# the variables.
i = 0
j = 0
sleep_timer = 0.5
list_length = len(numbers)

# repeat until all numbers are sorted.
for j in range(0, list_length-1):

    # repeat until end of list length reached.
    for i in range(0, list_length-1):

        # the numbers in the list.
        left = numbers[i]
        right = numbers[i+1]

        # switch position of numbers if left is bigger that right.
        if left > right:
            numbers[i] = right
            numbers[i+1] = left
            print(f"Switch: {numbers}")

            # only for humans to keep track.
            time.sleep(sleep_timer)
        i += 1
    j += 1