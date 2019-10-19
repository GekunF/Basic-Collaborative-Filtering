# -*- coding: utf-8 -*-

import numpy as np

"""
Class Used for calculating similarities
"""

class similarity(object):
	
    def __init__(self, max_2d, max_3d):
        '''
        initialize similarity calculator, which used for similarity measurements
        
        Parameters
        ----------
        max_2d: np.ndarray(maximum 2D, should support 1D, 2D)
            max_2d is the input for test data
        max_3d: np.ndarray(maximum 3D, should support 1D, 2D, 3D)
            max_3d is the input for train data
        '''
        assert(type(max_2d) == np.ndarray)
        assert(type(max_3d) == np.ndarray)
        assert(len(max_3d.shape) >= len(max_2d.shape))
        # TODO
        pass
    

    def sim(method_name = "cosine"):
        '''
        calculate similarity by using a defined method
        
        Parameters
        ----------
        method_name: str | "cosine"
        '''
        assert(type(method_name) == str)
        # TODO
        return similarity

    def cosine_similarity(self):
        '''
        calculate cosine similarity
        '''
        # TODO
        pass
    