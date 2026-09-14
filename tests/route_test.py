def test_home_page(client):
    """Test that the main index route loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"See the World" in response.data 

def test_recognize_get_route(client):
    """Test that the recognize upload page renders."""
    response = client.get('/recognize')
    # Because of the blueprint change, you might need to check the specific blueprint prefix if it redirects
    assert response.status_code in [200, 302] 

def test_recognize_post_no_file(client):
    """Test the form logic when a user submits without attaching an image."""
    response = client.post('/recognize', data={})
    # Your logic redirects the user back to the upload page (302) if no file is found
    assert response.status_code == 302