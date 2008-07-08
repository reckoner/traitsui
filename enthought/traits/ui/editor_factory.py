#------------------------------------------------------------------------------
#
#  Copyright (c) 2005, Enthought, Inc.
#  All rights reserved.
#  
#  This software is provided without warranty under the terms of the BSD
#  license included in enthought/LICENSE.txt and may be redistributed only
#  under the conditions described in the aforementioned license.  The license
#  is also available online at http://www.enthought.com/licenses/BSD.txt
#
#  Thanks for using Enthought open source!
#  
#  Author: David C. Morrill
#  Date:   10/07/2004
#
#------------------------------------------------------------------------------

""" Defines the abstract EditorFactory class, which represents a factory for
    creating the Editor objects used in a Traits-based user interface.
"""

#-------------------------------------------------------------------------------
#  Imports:
#-------------------------------------------------------------------------------

from enthought.traits.api \
    import HasPrivateTraits, Callable, Str, Bool

#-------------------------------------------------------------------------------
#  'EditorFactory' abstract base class:
#-------------------------------------------------------------------------------

class EditorFactory ( HasPrivateTraits ):
    """ Represents a factory for creating the Editor objects in a Traits-based
        user interface.
    """
    
    #---------------------------------------------------------------------------
    #  Trait definitions:
    #---------------------------------------------------------------------------
    
    # Function to use for string formatting
    format_func = Callable
    
    # Format string to use for formatting (used if **format_func** is not set).
    format_str = Str
    
    # Is the editor being used to create table grid cells?
    is_grid_cell = Bool( False )
    
    # Are created editors initially enabled?
    enabled = Bool( True )
    
    # The extended trait name of the trait containing editor invalid state
    # status:
    invalid = Str

    #---------------------------------------------------------------------------
    #  Initializes the object:
    #---------------------------------------------------------------------------
    
    def __init__ ( self, *args, **traits ):
        """ Initializes the factory object.
        """
        HasPrivateTraits.__init__( self, **traits )
        self.init( *args )
        
    #---------------------------------------------------------------------------
    #  Performs any initialization needed after all constructor traits have 
    #  been set:
    #---------------------------------------------------------------------------
     
    def init ( self ):
        """ Performs any initialization needed after all constructor traits 
            have been set.
        """
        pass
                         
    #---------------------------------------------------------------------------
    #  Returns the value of a specified extended name of the form: name or 
    #  context_object_name.name[.name...]:
    #---------------------------------------------------------------------------
                                                      
    def named_value ( self, name, ui ):
        """ Returns the value of a specified extended name of the form: name or 
            context_object_name.name[.name...]:
        """
        names = name.split( '.' )
        
        if len( names ) == 1:
            # fixme: This will produce incorrect values if the actual Item the
            # factory is being used with does not use the default object='name'
            # value, and the specified 'name' does not contain a '.'. The 
            # solution will probably involve providing the Item as an argument,
            # but it is currently not available at the time this method needs to 
            # be called...
            names.insert( 0, 'object' )
            
        value = ui.context[ names[0] ]
        for name in names[1:]:
            value = getattr( value, name )
            
        return value
    
    #---------------------------------------------------------------------------
    #  'Editor' factory methods:
    #---------------------------------------------------------------------------
    
    def simple_editor ( self, ui, object, trait_name, description, parent ):
        """ Generates an editor using the "simple" style.
        """
        raise NotImplementedError
    
    def custom_editor ( self, ui, object, trait_name, description, parent ):
        """ Generates an editor using the "custom" style.
        """
        raise NotImplementedError
    
    def text_editor ( self, ui, object, trait_name, description, parent ):
        """ Generates an editor using the "text" style.
        """
        raise NotImplementedError
    
    def readonly_editor ( self, ui, object, trait_name, description, parent ):
        """ Generates an "editor" that is read-only.
        """
        raise NotImplementedError

