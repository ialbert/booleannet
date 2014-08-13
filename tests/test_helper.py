# import path fixup
import sys
sys.path.append( '..' )

import unittest
from boolean import Model, helper, util

class HelperTest( unittest.TestCase ):
    
    def setUp(self):
        self.params = helper.read_parameters(  'test-params.csv' )
    
    def test_fixup( self ):
        "Tests knockout and overexpression"

        before = """
        A = B = C 1
        A* = A
        2: B* = B
        3:C* = C
        4: D* = D
        """

        text = util.modify_states(text=before, turnon=["A", "B"], turnoff=[ "C" , "V" ])

        after = """A = B = C 1.0
        C=False
        V=False
        A=True
        B=True
        #1: A * = A
        #2: B * = B
        #3: C * = C
        4: D * = D"""
        
        after = [ line.strip() for line in after.splitlines() ]
        after = '\n'.join( after)
        
        self.assertEqual( text, after )

    def test_parameter_reader( self ):
        "Testing reader"
        equal = self.assertEqual
        
        # take the first row of parameters
        active = self.params[0]
        
        # can be written in both ways
        equal ( active.Call.status, 'good' )
        equal ( active['Call']['status'], 'good' )

        equal ( active.PIC.conc, 0.9 )
        equal ( active['PIC']['conc'], 0.9 )

        equal ( active.PIC.decay, 1.0 )
        equal ( active['PIC']['decay'], 1.0 )

        # test second row
        active = self.params[1]
        
        equal ( active.MP.gamma, 0.234 )
        equal ( active['MP']['gamma'], 0.234 )

        equal ( active.MP.n, 2 )
        equal ( active['MP']['n'], 2 )

        equal ( active.Call.status, 'marginal' )
        equal ( active['Call']['status'], 'marginal' )

        equal ( active['Ca+2']['levels'], 3.5 )

    def test_function_initializer( self ):
        "Testing function initializer"
        text = """
        MP = True
        1: PIC* = PIC
        1: MP* = PIC and MP
        """
        data = self.params[1]
        eng  = Model( mode='plde', text=text )
        eng.initialize( missing=helper.initializer( data ) )

        for node in 'PIC'.split():
            values = ( data[node].conc, data[node].decay, data[node].threshold )
            self.assertEqual( eng.start[node], values )

    def test_default_initializer( self ):
        "Testing default initializer"
        text = """
        ABC3 = (1, 2, 3)
        1: ABC1* = ABC
        1: ABC2* = ABC1 and ABC2
        """
        data = self.params[1]
        eng  = Model( mode='plde', text=text )
        eng.initialize( missing=helper.initializer( data, default=(1,1,1) ) )

        for node in 'ABC1 ABC2'.split():
            self.assertEqual( eng.start[node], (1, 1, 1) )
        
        self.assertEqual( eng.start['ABC3'], (1.0, 2.0, 3.0) )


def get_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase( HelperTest )
    return suite

if __name__ == '__main__':
    unittest.TextTestRunner( verbosity=2 ).run( get_suite() )  

    fname  = 'test-params.csv'
        
    # this contains all parameters
    params = helper.read_parameters( fname )

    #print params[0].PIC['conc']

