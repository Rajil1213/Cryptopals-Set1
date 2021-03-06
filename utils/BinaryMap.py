from math import log2
from sys import exit

class BinaryMap:

    @classmethod
    def getBinary(cls, n=6):
        """ Gets upto n-bits of binary values in order
            For example, n=2 gives ["00", "01", "10", "11"]
        Args:
            n (int, optional): [no of bits]. Defaults to 6.
        Returns:
            [string]: [list of `n` bits of binary numbers as string, in order]
        """

        twoBit = ["00", "01", "10", "11"]
        sixBit = ""
        sixBitBinary = []

        for firstCrumb in twoBit:
            for secondCrumb in twoBit:
                for thirdCrumb in twoBit:
                    sixBit = firstCrumb + secondCrumb + thirdCrumb
                    sixBitBinary.append(sixBit)

        if n == 6:
            return sixBitBinary
        
        start = 6 - n
        nBits = sixBitBinary[:2**n]
        nBitBinary = [value[start:] for value in nBits]

        return nBitBinary
    
    @classmethod
    def getBinaryMapping(cls, charset):
        """Maps the characters in charset to their corresponding binary value, in order,
        starting from 0
        Args:
            charset (string): the string of characters to map
        Returns:
            dict: dict() that maps each character in `charset` to a unique binary value
        """

        n = len(charset)

        if not n % 2 == 0:
            print("No. of chars in charset must be even")
            exit(1)

        noOfBits = int(log2(n))
        binaryBits = cls.getBinary(noOfBits)

        mapping = dict()
        for i in range(n):
            key = charset[i]
            binaryVal = binaryBits[i]
            mapping[key] = binaryVal
        
        return mapping
    
    @classmethod
    def binaryToBase64(cls, binary):
        """converts a string of bits to its base64-encoded version and returns it
        Args:
            binary (string): a string of bits to convert
        Returns:
            [string]: a string representing the base64 encoding of `binary`
        """ 

        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        specials = "+/"
        base64Charset = uppercase + lowercase + numbers + specials 
        binary2base64 = cls.getBinaryMapping(base64Charset)
        binary2base64 = { value: key for (key, value) in binary2base64.items()}        
        base64Equivalent = ""

        padding = 0
        if len(binary) % 6 != 0:
            padding = 6 - (len(binary) % 6)
        
        zeros = '0' * padding
        equals = '=' * (padding // 2)

        binary += zeros
        n = len(binary)

        for i in range(0, n, 6):
            binaryVal = binary[i:i + 6]
            base64Equivalent += binary2base64[binaryVal]
            
        base64Equivalent += equals
        
        return base64Equivalent
    
    @classmethod
    def base64ToBinary(cls, base64):
        """convert a base64 encoded string into a string of its equivalent binary

        Args:
            base64 (str): a base64 encoded string

        Returns:
            str: corresponding string of bits
        """
        
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        specials = "+/"
        base64Charset = uppercase + lowercase + numbers + specials 
        base642Binary = cls.getBinaryMapping(base64Charset)
        binaryEquivalent = ""

        equals = base64.count('=')
        padded = equals * 2
        base64 = base64.rstrip('=')

        for char in base64:
            binary = base642Binary[char]
            binaryEquivalent += binary
        
        # remove padded zeros
        if padded > 0:
            binaryEquivalent = binaryEquivalent[:-padded]
        
        return binaryEquivalent
