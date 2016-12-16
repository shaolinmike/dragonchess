"""
This module defines the different game pieces.

*Todo:*
	* Enter thing to do. (optional field)

*Author:*
	* Mitri Van, mitri.van@volition-inc.com, 9/30/2013 4:12:33 PM
"""


# Boards

##############
# Upper board
##############

##############
# Middle board
##############

##############
# Lower board
##############


# Pieces
'''
###########
Upper board
###########

   The Sylph (S)

   	On level 3:

      	can move one step diagonally forward, or capture one step straight forward;[note 1]
      	can captureOn the square directly belowOn level 2.

   	On level 2:

      	can move to the square directly aboveOn level 3, or to one of the player's six Sylph starting squares.

   The Griffon (G)

      On level 3:

      	can move and capture by jumping[note 2] in the following pattern: two steps diagonally followed by one step orthogonally outward;[note 3]
      	can move and capture one step triagonally to level 2.[note 4]

      On level 2:

      	can move and capture one step diagonally;
      	can move and capture one step triagonally to level 3.[note 5]

   The Dragon (R)

      Bound to level 3:

			can move and capture any number of unobstructed steps diagonally, or one step orthogonally;[note 6]
			can capture remotely (without leaving level 3)On the square directly belowOn level 2, orOn any square orthogonally adjacent to that square.

############
Middle board
############

The Warrior (W)

   Bound to level 2:

     	can move one step straight forward, or capture one step diagonally forward;[note 7]
      promotes to Hero when reaching the 8th rank.

The Oliphant (O)

   Bound to level 2:

     	can move and capture any number of unobstructed steps orthogonally.[note 8]

The Unicorn (U)

   Bound to level 2:

     	can move and capture the same as a chess knight.

The Hero (H)

   On level 2:

     	can move and capture one or two unblockable steps diagonally;
     	can move and capture one step triagonally to levels 1 or 3.[note 5][note 4]

   On levels 1 and 3:

     	can move and capture one step triagonally to the same squareOn level 2 the Hero previously left.

The Thief (T)

   Bound to level 2:

     	can move and capture any number of unobstructed steps diagonally.[note 9]

The Cleric (C)

   On any level:

     	can move and capture one step in any direction;[note 10]
     	can move and capture to the square directly above or directly belowOn an adjacent level.

The Mage (M)

   On level 2:

     	can move and capture any number of unobstructed steps diagonally or orthogonally.[note 11]

   On levels 1 and 3:

     	can move one step orthogonally.[note 12]

   On any level:

     	can move and capture one or two steps directly above or directly below to one of the other levels.[note 13]

The King (K)

   On level 2:

     	can move and capture one step in any direction;[note 10]
     	can move and capture to the square directly belowOn level 1 or directly aboveOn level 3.

   On levels 1 and 3:

     	can move to (only) the same squareOn level 2 the King previously left.[note 12]

The Paladin (P)

   On level 2:

     	can move and capture as a chess king+knight;
     	can move to levels 1 or 3 using an (unblockable) knight-like move: one level up or down followed by two steps orthogonally.

   On levels 1 and 3:

     	can move and capture one step in any direction;[note 10]
     	can move to the other levels using an (unblockable) knight-like move: one level up or down followed by two steps orthogonally, or two levels up or down followed by one step orthogonally.


###########
Lower board
###########

The Dwarf (D)

   On level 1:

     	can move one step straight forward or sideways, or capture one step diagonally forward;
     	can captureOn the square directly aboveOn level 2.

   On level 2:

     	can move one step straight forward or sideways, or capture one step diagonally forward;
     	can move to the square directly belowOn level 1.

The Basilisk (B)

   Bound to level 1:

     	can move one step diagonally forward or straight backward, or capture one step straight forward;
      always freezes (immobilizes) an enemy pieceOn the square directly aboveOn level 2.

The Elemental (E)

   On level 1:

     	can move and capture one or two steps orthogonally;[note 13]
     	can move one step diagonally;
     	can capture in the following pattern: one step orthogonally followed by the square directly aboveOn level 2.[note 13]

   On level 2:

     	can move and capture in the following pattern: the square directly belowOn level 1 followed by one step orthogonally.

*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   | B |   |   |   | E |   |   |   | B |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   | d |   | d |   | d |   | d |   | d |   | d |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   |   |   |   |   |   |   |   |   |   |   |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   | d |   | d |   | d |   | d |   | d |   | d |
*---*---*---*---*---*---*---*---*---*---*---*---*
|   |   | B |   |   |   | E |   |   |   | B |   |
*---*---*---*---*---*---*---*---*---*---*---*---*

 111 112 113 114 115 116 117 118 119 120
 101 102 103 104 105 106 107 108 109 110
  91  92  93  94  95  96  97  98  99 100
  71  72  73  74  75  76  77  78  79  80
  51  52  53  54  55  56  57  58  59  60
  41  42  43  44  45  46  47  48  49  50
  31  32  33  34  35  36  37  38  39  40
  21  22  23  24  25  26  27  28  29  30
  11  12  13  14  15  16  17  18  19  20
  01  02  03  04  05  06  07  08  09  10

 '''