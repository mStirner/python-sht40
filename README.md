# Description
Quick demo code for debugging/sharing. <br />
The python example does not work, the c example does.<br />
Python exit with "error no. 5, input/output error".<br >
Even `i2cget -y 1 0x44` fails with `Error: Read failed` but the sensor is correct detected `i2cdetect -y 1`:

```
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:                         -- -- -- -- -- -- -- -- 
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
20: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
40: -- -- -- -- 44 -- -- -- -- -- -- -- -- -- -- -- 
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- 
70: -- -- -- -- -- -- -- --          
```


[`read-sht40-1.py`](./read-sht40-1.py) & [`read-sht40-2.py`](./read-sht40-2.py) are two diffrent approaches to get data from the sensor.<br />
- "1" the first appraoch, with out the "special" stuff that the working c code contains. 
- "2" with the special things like "soft reset" & "lower precision".


# Links
- Manufacturer example/driver repo: https://github.com/Sensirion/raspberry-pi-i2c-sht4x/tree/master
- Sensor: https://de.aliexpress.com/item/1005004731609010.html?spm=a2g0o.order_list.order_list_main.5.7cfb5c5ffvx3ms&gatewayAdapt=glo2deu