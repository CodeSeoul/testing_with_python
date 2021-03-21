def test_list_names(client, sample_name):
    response = client.get('/names/')
    assert response.status_code == 200

    result = response.json()
    assert 'names' in result
    name_list = result['names']
    assert len(name_list) > 0
    assert 'id' in name_list[0]
    assert 'name' in name_list[0]
    found_sample = False
    for name in name_list:
        if name == sample_name:
            found_sample = True
    assert found_sample


def test_get_name(client, sample_name):
    response = client.get(f'/names/{sample_name["id"]}/')
    assert response.status_code == 200

    result = response.json()
    assert result == sample_name


def test_create_name(client, generated_name_text, cleanup_name):
    response = client.post(
        '/names/',
        json={'name': generated_name_text}
    )
    assert response.status_code == 200

    result = response.json()
    assert 'id' in result
    cleanup_name(result['id'])
    assert result['name'] == generated_name_text
