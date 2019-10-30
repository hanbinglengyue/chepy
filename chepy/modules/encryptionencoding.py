import codecs
import string

from ..core import Core


class EncryptionEncoding(Core):
    def rotate(self, rotate_by: int) -> "Baked":
        lc = string.ascii_lowercase
        uc = string.ascii_uppercase
        lookup = str.maketrans(
            lc + uc, lc[rotate_by:] + lc[:rotate_by] + uc[rotate_by:] + uc[:rotate_by]
        )
        self._holder = self._holder.translate(lookup)
        return self

    def rot_13(self) -> "Baked":
        """A simple caesar substitution cipher which rotates alphabet 
        characters by the specified amount (default 13).
        
        Returns
        -------
        Baked
            The Baked object. 
        """
        self._holder = codecs.encode(self._convert_to_str(), "rot_13")
        return self

    def rot_47(self) -> "Baked":
        """A slightly more complex variation of a caesar cipher, which includes 
        ASCII characters from 33 '!' to 126 '~'. Default rotation: 47.
        
        Returns
        -------
        Baked
            The Baked object. 
        """
        x = []
        for i in range(len(self._holder)):
            j = ord(self._holder[i])
            if j >= 33 and j <= 126:
                x.append(chr(33 + ((j + 14) % 94)))
            else:
                x.append(self._holder[i])
        self._holder = "".join(x)
        return self
