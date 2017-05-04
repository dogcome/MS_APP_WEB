# -*- coding: utf-8 -*-

STATUSES = [
    ['1', 'Active'],
    ['2', 'Stop'],
    ['3', 'Out'],
    ['4', 'getBack'],
]

db.define_table(
    'partTime',

    Field('PTname', length=25, requires=[IS_NOT_EMPTY(), Titleize()]),
    Field('PTnuber', length=50, label='PTnuber'),
    
    Field('PTowener', 'reference auth_user'),

   
    Field('addr_city', length=50, label='City'),
    Field('addr_state', length=50, label='State/Province'),
    

    Field('phone', length=50, label='Phone'),
    Field('fax', length=50, label='Fax'),

    Field('string_list', length=25,
          requires=IS_IN_SET(['Regional', 'Corporate', 'Local', 'Other'], zero=None)),
    Field('status', 'integer', label='Status',
          requires=IS_IN_SET(STATUSES, zero=None)),

    auth.signature,
    singular='Part Time Jod Mser', plural='Part Time Jod Msers',
    format='%(title)s',
)


