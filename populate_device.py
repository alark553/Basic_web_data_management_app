import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'basic_app.settings')

import django
django.setup()

from device_list.models import Device


def populate():
    

    add_device(name='Integrated Observation Equipment',
        device_range=2000
 		)

    add_device(name='Passive Night Vision Binocular (Mk-I)',
        device_range=500
 		)

    add_device(name='Passive Night Vision Goggles',
        device_range=225
 		)

    add_device(name='Passive Night Sight for 84 mm Carl',
        device_range=500
 		)

    add_device(name='Passive Night Sight for 5.56 mm Rifle',
        device_range=200
 		)

    add_device(name='Passive Night Sight for 5.56 mm LMG',
        device_range=200
 		)

    add_device(name='Passive Night Sight RCL Mk I',
        device_range=600
 		)

    add_device(name='Passive Night Sight RCL Mk II',
        device_range=600
 		)

    add_device(name='Driver Sight for T-55',
        device_range=100
 		)

    add_device(name='Gunners Night Sight for T-55',
        device_range=800
 		)

    add_device(name='Balloon Lifted Imaging & Surveillance',
        device_range=4000
 		)
    add_device(name='Goggles for Aireforce',
        device_range=250
 		)

    add_device(name='Sight for 84 Mm',
        device_range=700
		)


    # Print out what we have added to the user.
    for d in Device.objects.all():
        print "- {0} - {1}".format(d.name,d.device_range)

def add_device(name, device_range):
    d = Device.objects.get_or_create(name=name,device_range=device_range)[0]
    return d



# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()

