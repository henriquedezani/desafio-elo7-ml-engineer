import unittest
from api import app as api_app
import os
import cloudpickle
from sklearn.pipeline import Pipeline
import json

with open(os.getenv("MODEL_PATH"), 'rb') as model_file:
    model = cloudpickle.load(model_file)

class TestHome(unittest.TestCase):

    def test_load_model(self):
        self.assertEqual(Pipeline, model.__class__)

    def test_word2vec_transform(self):
        y_pred = model['text_transform'].transform(['Lembrancinhas'])
        self.assertTupleEqual(y_pred.shape, (1, 300) )

    def test_classification(self):
        predict = model.predict(['Lembrancinhas'])
        self.assertListEqual(predict.tolist(), ['Lembrancinhas'])

    def test_post_success_status_code(self):        
        request_params = dict(products = [dict(title = "Lembrancinha")])
        app = api_app.test_client()
        self.response = app.post('/v1/categorize', data=json.dumps(request_params),content_type='application/json')
        self.assertEqual(200, self.response.status_code)

    def test_post_fail_status_code(self):
        request_params = dict(products = [])
        app = api_app.test_client()
        self.response = app.post('/v1/categorize', data=json.dumps(request_params),content_type='application/json')
        self.assertEqual(400, self.response.status_code)

    def test_post_categorize(self):
        request_params = dict(products = [dict(title = "Lembrancinha"), dict(title = "Carrinho de Bebê")])
        expected_response = dict(categories = [ 'Lembrancinhas', 'Bebê'])
        app = api_app.test_client()
        self.response = app.post('/v1/categorize', data=json.dumps(request_params),content_type='application/json')
        self.assertDictEqual(expected_response, dict(self.response.get_json()))

if __name__ == '__main__':
    unittest.main()