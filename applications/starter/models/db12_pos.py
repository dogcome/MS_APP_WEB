# -*- coding: utf-8 -*-

STATUSES = [
    ['1', 'Active'],
    ['2', 'Stop'],
    
]

db.define_table(
    'pos',
    Field('PROVINCE', length=50, label='State/Province'),
    Field('CITY', length=50, label='City'),
    Field('posCode', length=25),
    
    
    Field('POS_TYPE', length=25,
          requires=IS_IN_SET(['AP', 'Satelitte', 'ALDI'], zero=None)),

    Field('POS_COMODITY', length=25,
          requires=IS_IN_SET(['CAR', 'CELL_PHONE', 'PC_FAC','MBT','MOT','HA','EMTB_MTB'], zero=None)),
    
    Field('POS_name', length=25, requires=[IS_NOT_EMPTY()]),
    Field('POS_address', length=50, label='Street'),
    Field('Bus_station', length=50, label='station'),
    Field('Landmark', length=50, label='Closest Landmark and location'),
    Field('Shop_Name', length=50, label='shop'),
    
    Field('POS_REGISTRATION_Number', length=50, label='regNo'),
    Field('POS_AREA', length=50, label='Area'),
    Field('POS_Phone', length=50, label='Phone'),
        
    Field('status', 'integer', label='Status',
          requires=IS_IN_SET(STATUSES, zero=None)),
          
    Field('LONGITUDE', length=50, label='lon'),
    Field('LATITUDE', length=50, label='lat'),
    
    

    auth.signature,
    singular='POS', plural='All_POS',
    format='%(title)s',
)


