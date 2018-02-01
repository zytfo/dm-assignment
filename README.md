This file contains 9 sets of sanitized user data drawn from the
command histories of 8 UNIX computer users at Purdue over the course
of up to 2 years (USER0 and USER1 were generated by the same person,
working on different platforms and different projects).  The data is
drawn from tcsh(1) history files and has been parsed and sanitized to
remove filenames, user names, directory structures, web addresses,
host names, and other possibly identifying items.  Command names,
flags, and shell metacharacters have been preserved.  Additionally,
**SOF** and **EOF** tokens have been inserted at the start and end of
shell sessions, respectively.  Sessions are concatenated by date order
and tokens appear in the order issued within the shell session, but no
timestamps are included in this data.  For example, the two sessions:

	# Start session 1
	cd ~/private/docs
	ls -laF | more
	cat foo.txt bar.txt zorch.txt > somewhere
	exit
	# End session 1

	# Start session 2
	cd ~/games/
	xquake &
	fg
	vi scores.txt
	mailx john_doe@somewhere.com
	exit
	# End session 2
	
would be represented by the token stream
	
	**SOF**
	cd
	<1>			# one "file name" argument
	ls
	-laF
	|
	more
	cat
	<3>			# three "file" arguments
	>
	<1>
	exit
	**EOF**
	**SOF**
	cd
	<1>
	xquake
	&
	fg
	vi
	<1>
	mailx
	<1>
	exit
	**EOF**


This data is made available under conditions of anonymity for the
contributing users and may be used for research purposes only.
Summaries and research results employing this data may be published,
but literal tokens or token sequences from the data may not be
published except with express consent of the originators of the data.
No portion of this data may be released with or included in a
commercial product, nor may any portion of this data be sold or
redistributed for profit or as part of of a profit-making endeavor.

Please direct any questions regarding this data to Terran Lane:
terran@ecn.purdue.edu.
# dm-assignment