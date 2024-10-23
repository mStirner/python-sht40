// content from https://github.com/Sensirion/raspberry-pi-i2c-sht4x/blob/827259f2430e425cf28d9daab16827101dca8001/example-usage/sht4x_i2c_example_usage.c

#include "sensirion_common.h"
#include "sensirion_i2c_hal.h"
#include "sht4x_i2c.h"
#include <inttypes.h>  // PRIx64
#include <stdio.h>     // printf

#define sensirion_hal_sleep_us sensirion_i2c_hal_sleep_usec

int main(void) {
    int16_t error = NO_ERROR;
    sensirion_i2c_hal_init();
    sht4x_init(SHT40_I2C_ADDR_44);

    sht4x_soft_reset();
    sensirion_hal_sleep_us(10000);
    uint32_t serial_number = 0;
    error = sht4x_serial_number(&serial_number);
    if (error != NO_ERROR) {
        printf("error executing serial_number(): %i\n", error);
        return error;
    }
    printf("serial_number: %u\n", serial_number);
    float a_temperature = 0.0;
    float a_humidity = 0.0;
    uint16_t repetition = 0;
    for (repetition = 0; repetition < 500; repetition++) {
        sensirion_hal_sleep_us(20000);
        error = sht4x_measure_lowest_precision(&a_temperature, &a_humidity);
        if (error != NO_ERROR) {
            printf("error executing measure_lowest_precision(): %i\n", error);
            continue;
        }
        printf("a_temperature: %.2f ", a_temperature);
        printf("a_humidity: %.2f\n", a_humidity);
    }

    return NO_ERROR;
}
