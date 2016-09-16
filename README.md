
Data Wrangling
===============

District Margins 
----------------------------

In the US, our legislature is made up of representatives of individual
*districts* (unlike proportional representation systems).  Some of
these districts are competitive, meaning that the winner of the
election is not a "sure thing" based on the voters in the districts.
However, for a variety of reasons, many of these districts are not
very competitive.  We're going to look at the 2014 election and see
which districts are competitive.  This also gives us a chance to play
around with some continuous data (well, sort of; we'll assume votes
are continuous even though you can't have a fractional vote).

You will output to a file with the districts sorted by how competitive
they are (with the most competitive districts first).  If an election
is uncontested, the margin should be "100", in that the percentage
difference between the first place candidate and the second is 100.  

    $ python districts.py
    $ head district_totals.csv
    STATE,DISTRICT,MARGIN
    Arizona,2,0.07000000000000028
    California,7,0.7999999999999972
    Florida,2,1.1299999999999955
    Minnesota,8,1.3999999999999986
    Maryland,6,1.4500000000000028
    California,16,1.4599999999999937
    Washington,4,1.6200000000000045
    Texas,23,2.1000000000000014
    Iowa,1,2.280000000000001
    $ tail district_totals.csv
    Georgia,3,100.0
    Georgia,14,100.0
    Florida,25,100
    Georgia,5,100.0
    Florida,14,100
    Georgia,11,100.0
    Pennsylvania,18,100.0
    West Virginia,5,100.0
    West Virginia,4,100.0
    Florida,27,100

You should not need to modify the "main" function.

Words Presidents Use 
-------------------------------

Each year, the president of the United States is required to make a
speech to congress describing the "State of the Union".  You will
count the most frequent words in all of the past addresses (we'll do
more interesting things with this later).

We've placed all of these in a zip file, with each speech as a
separate fill inside the zip archive.  To complete this assignment,
you'll need to go through each of the files, find the words, and then
sum them up.  This has been broken down into three functions you'll
need to complete:
* text_from_zipfile
* words
* accumulate_counts

We define a word as four or more contiguous characters in the range
a-z or A-Z.  The resulting words should be lower case.  This removes
punctuation, short words, and other distracting information from the
files.

Course info
-----------------------
FA2016 CSCI3022
