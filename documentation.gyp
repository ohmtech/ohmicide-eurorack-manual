##############################################################################
#
#     documentation.gyp
#     Copyright (c) 2024 Raphael DINGE
#
#Tab=3########################################################################



{
   'targets' : [
      {
         'target_name': 'documentation',
         'type': 'none',

         'sources': [
            'README.md',
            'index.md',
            'installation/index.md',
            'specifications/index.md',
            'overview/index.md',
            'functions/index.md',
            'modes/index.md',
            'system/index.md',
            'update/index.md',
            'factory/index.md',
            'reference/index.md',
            'changelog/index.md',
         ],
      },
   ],
}
