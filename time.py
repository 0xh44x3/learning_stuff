"""
    Copyright 2021 by Sebastian Haacke

    time.py - Get current time and add some hours, maybe useful for
    creating links that expire

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

import time, datetime, os

# clear screen.
from typing import List

# clear screen at beginning.
def clear_console():
    os.system('clear')

clear_console()


def get_time():
    # get the current time.
    current_time = datetime.datetime.now()

    # add 2 hours (in seconds) to current_time
    future_time = current_time + datetime.timedelta(hours = 1)

    if current_time < future_time:
        print(f"Time account created : {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Time link will expire: {future_time.strftime('%Y-%m-%d %H:%M:%S')}")
    else:
        print("Link expired")

get_time()