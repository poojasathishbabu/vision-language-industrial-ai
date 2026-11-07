from src_model_vit import describe
def test_describe():
    r=describe('sample.jpg','Describe defects'); assert r['confidence']>0.9 and 'defect' in r
