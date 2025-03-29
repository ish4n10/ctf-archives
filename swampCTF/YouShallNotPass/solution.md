## Solution

The binary is quite simple, it does alot of things but we don't need to actually mind it. The only thing interesting was a function being called by it's address.

It takes the input and does some operations in it one-byte-at-a-time and compares it to a constant. We can simple reverse the operations as they are 'xored'.