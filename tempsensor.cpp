#include 
#include "DS18S20.h"
#include "DS18B20.h"
#include "OneWireDefs.h"

//#define THERMOMETER DS18S20
#define THERMOMETER DS18B20

int main()
{
    //          device( crcOn, useAddress, parasitic, mbed pin )
    THERMOMETER device(true, true, false, p25);
    
    while (!device.initialize());    // keep calling until it works
    
    while (true)
    {
        // changing the resolutions only affects the DS18B20. The DS18S20 is fixed.
        device.setResolution(nineBit);
        device.readTemperature(); 
        wait(5);
        device.setResolution(tenBit);
        device.readTemperature(); 
        wait(5);
        device.setResolution(elevenBit);
        device.readTemperature(); 
        wait(5);
        device.setResolution(twelveBit);
        device.readTemperature(); 
        wait(5);
    }
     
    return EXIT_SUCCESS;
}
