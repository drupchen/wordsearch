#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2008, Samiuela Loni Vea Taufa
# All rights reserved.
#
# see LICENSE.TXT for license/copyright information
import string, unicodedata
from lang import Language

class to(Language):
    def __init__(self, list=""):
        Language.__init__(self)
        self.initCharSet()
        self.initCharSetExt()
        self.initGlottals()
        self.c_addCharacters(self.diacritics_all) # Compromise for mis-typed documents
        self.c_addCharacters(self.glottals_all) # Compromise for mis-typed documents
        self.c_addCharacters(string.letters) # Compromise for non-Tongan words        
    def initCharSet(self):
        self.voweldiacritics = (
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH ACUTE')
            ) + (
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON')
            )
        self.validVowels = (
            unicodedata.lookup('LATIN SMALL LETTER A') +
            unicodedata.lookup('LATIN SMALL LETTER E') +
            unicodedata.lookup('LATIN SMALL LETTER I') +
            unicodedata.lookup('LATIN SMALL LETTER O') +
            unicodedata.lookup('LATIN SMALL LETTER U') +
            unicodedata.lookup('LATIN CAPITAL LETTER A') +
            unicodedata.lookup('LATIN CAPITAL LETTER E') +
            unicodedata.lookup('LATIN CAPITAL LETTER I') +
            unicodedata.lookup('LATIN CAPITAL LETTER O') +
            unicodedata.lookup('LATIN CAPITAL LETTER U') +
            self.voweldiacritics
        )
        self.validConsonants = (
            unicodedata.lookup('LATIN SMALL LETTER F') +
            unicodedata.lookup('LATIN SMALL LETTER H') +
            unicodedata.lookup('LATIN SMALL LETTER K') +
            unicodedata.lookup('LATIN SMALL LETTER L') +
            unicodedata.lookup('LATIN SMALL LETTER M') +
            unicodedata.lookup('LATIN SMALL LETTER N') +
            unicodedata.lookup('LATIN SMALL LETTER G') +
            unicodedata.lookup('LATIN SMALL LETTER P') +
            unicodedata.lookup('LATIN SMALL LETTER S') +
            unicodedata.lookup('LATIN SMALL LETTER T') +
            unicodedata.lookup('LATIN SMALL LETTER V') +
            unicodedata.lookup('LATIN CAPITAL LETTER F') +
            unicodedata.lookup('LATIN CAPITAL LETTER H') +
            unicodedata.lookup('LATIN CAPITAL LETTER K') +
            unicodedata.lookup('LATIN CAPITAL LETTER L') +
            unicodedata.lookup('LATIN CAPITAL LETTER M') +
            unicodedata.lookup('LATIN CAPITAL LETTER N') +
            unicodedata.lookup('LATIN CAPITAL LETTER G') +
            unicodedata.lookup('LATIN CAPITAL LETTER P') +
            unicodedata.lookup('LATIN CAPITAL LETTER S') +
            unicodedata.lookup('LATIN CAPITAL LETTER T') +
            unicodedata.lookup('LATIN CAPITAL LETTER V') 
        )
        self.glottals_to  = unicodedata.lookup('MODIFIER LETTER TURNED COMMA')
            # unicodedata.lookup('LEFTER SINGLE QUOTATION MARK') # when character not available

        self.charSet = (
            self.validConsonants + self.validVowels + self.glottals_to
#           + unicodedata.lookup('FULL STOP')
        )
    def initGlottals(self):
        self.glottals_all = (unicodedata.lookup('APOSTROPHE') +
                             unicodedata.lookup('GRAVE ACCENT') +
                             unicodedata.lookup('ACUTE ACCENT') +
                             unicodedata.lookup('MODIFIER LETTER TURNED COMMA') +
                             unicodedata.lookup('MODIFIER LETTER APOSTROPHE') +
                             unicodedata.lookup('MODIFIER LETTER REVERSED COMMA') +
                             unicodedata.lookup('MODIFIER LETTER ACUTE ACCENT') +
                             unicodedata.lookup('MODIFIER LETTER GRAVE ACCENT') +
                             unicodedata.lookup('COMBINING TURNED COMMA ABOVE') +
                             unicodedata.lookup('COMBINING REVERSED COMMA ABOVE') +
                             unicodedata.lookup('COMBINING COMMA ABOVE') +
                             unicodedata.lookup('COMBINING COMMA ABOVE RIGHT') +
                             unicodedata.lookup('COMBINING GRAVE TONE MARK') +
                             unicodedata.lookup('COMBINING ACUTE TONE MARK') +
                             unicodedata.lookup('LATIN LETTER GLOTTAL STOP') +
                             unicodedata.lookup('LATIN CAPITAL LETTER GLOTTAL STOP')
                             )
    
    def initCharSetExt(self):
        """Diacritical mark: a mark placed over, under, alongside or
        attached to a letter to indicate pronunciation, stress, or other value.
        """
        self.diacritics_all = (
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH CIRCUMFLEX') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH DIAERESIS') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH DIAERESIS') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH DIAERESIS') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH DIAERESIS') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH DIAERESIS') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH DIAERESIS') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH DIAERESIS') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH DIAERESIS') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH DIAERESIS') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH DIAERESIS') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH TILDE') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH TILDE') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH TILDE') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH TILDE') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH TILDE') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH TILDE') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH TILDE') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH TILDE') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH TILDE') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH TILDE') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH GRAVE') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH GRAVE') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH GRAVE') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH GRAVE') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH GRAVE') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH GRAVE') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH GRAVE') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH GRAVE') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH GRAVE') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH GRAVE') 
            )
        self.diacritics_to = (
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH ACUTE') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH ACUTE') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH ACUTE')
            ) + (
            unicodedata.lookup('LATIN CAPITAL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN CAPITAL LETTER U WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER A WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER E WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER I WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER O WITH MACRON') +
            unicodedata.lookup('LATIN SMALL LETTER U WITH MACRON')
            ) * 4


    
    def w_validFirst( self, letter):
        return True #
    def w_Tokens(self, line = None):
        if line is None:
            line = self.list_words
        
        iTokenStart = 0
        iPrev = 0
        iCurr = 0
        iMax  = len(line)
        Tokens = []
        
        wordConstructs = self.charSet + self.charSetExt
        
        for iCurr in range(0, iMax):
            letter = line[iCurr]
            if letter in wordConstructs:
                if iCurr == iMax-1: # last letter special exception
                    if letter not in self.glottals_all:
                        Tokens.append(line[iTokenStart:iMax])
                    else:
                        Tokens.append(line[iTokenStart:iMax-1])
                    
                elif letter in self.glottals_all:
                    if line[iCurr+1] in self.validVowels:
                        line = line[0:iCurr] + self.glottals_to + line[iCurr+1:]
                    elif iCurr == iTokenStart:
                        iTokenStart = iCurr + 1
                    else:
                        Tokens.append(line[iTokenStart:iCurr])
                        iTokenStart = iCurr + 1                        #    Tokens.append(line[iTokenStart:iCurr])
                        #    iTokenStart = iCurr + 1
            else:                
                if ( letter in self.glottals_all and
                     iCurr < iMax - 1 and line[iCurr + 1] in self.validVowels
                   ):
                    line = line.replace(line[0:iCurr+1],line[0:iCurr]+self.glottals_to,1)
                elif iCurr == iTokenStart: # We're still at the start
                    iTokenStart = iCurr + 1     # Ignore the error and start with the next letter
                else: # Word-boundary - grab the word prior to this location 
                    Tokens.append(line[iTokenStart:iCurr])
                    iTokenStart = iCurr + 1
            iPrev = iCurr
        return Tokens
    
if __name__ == "__main__":
    pass