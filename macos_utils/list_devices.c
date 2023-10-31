#include <stdio.h>
#include <libusb.h>

int main() {
    libusb_device **devs;
    libusb_context *ctx = NULL;
    int r;
    ssize_t cnt;

    r = libusb_init(&ctx);
    if(r < 0) {
        printf("Init Error %d\n", r);
        return 1;
    }

    cnt = libusb_get_device_list(ctx, &devs);
    if(cnt < 0) {
        printf("Get Device Error\n");
        return 1;
    }

    printf("%zd Devices in list.\n", cnt);

    libusb_device *dev;
    int i = 0;

    while ((dev = devs[i++]) != NULL) {
        struct libusb_device_descriptor desc;
        int r = libusb_get_device_descriptor(dev, &desc);
        if (r < 0) {
            printf("Failed to get device descriptor\n");
            return 1;
        }

        libusb_device_handle *handle = NULL;
        r = libusb_open(dev, &handle);
        if (r < 0) {
            printf("Cannot open device\n");
        } else {
            unsigned char string[256];
            printf("Device (VendorId:ProductId): %04x:%04x", desc.idVendor, desc.idProduct);
            if (desc.iManufacturer > 0) {
                r = libusb_get_string_descriptor_ascii(handle, desc.iManufacturer, string, sizeof(string));
                if (r > 0)
                    printf(", Manufacturer: %s", string);
            }
            if (desc.iProduct > 0) {
                r = libusb_get_string_descriptor_ascii(handle, desc.iProduct, string, sizeof(string));
                if (r > 0)
                    printf(", Product: %s", string);
            }
            if (desc.iSerialNumber > 0) {
                r = libusb_get_string_descriptor_ascii(handle, desc.iSerialNumber, string, sizeof(string));
                if (r > 0)
                    printf(", Serial Number: %s", string);
            }
            printf("\n");
            libusb_close(handle);
        }
    }

    libusb_free_device_list(devs, 1);
    libusb_exit(ctx);

    return 0;
}