#
# Fake test 3
#
# This file is part of Pints Functional Testing.
#  Copyright (c) 2017-2018, University of Oxford.
#  For licensing information, see the LICENSE file distributed with the Pints
#  functional testing software package.
#
from __future__ import absolute_import, division
from __future__ import print_function, unicode_literals

import pfunk


class Test3(pfunk.FunctionalTest):

    def __init__(self):
        super(Test3, self).__init__('test3')

    def _run(self, result, log_path):
        print('Running ' + self.name())
        result['status'] = 'done'

