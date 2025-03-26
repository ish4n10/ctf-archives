## Solution

If we do strings on the binary, we can a section named ".TRACES...", hex dumping it with 

```
objdump -s -j .TRACES_OF_THE_ZOGULAN hyperdrive_encoder.elf
``` 

 we can get the data. Then we just simply reverse the algorithm and apply it on the dumped data we got from the section.