import json
from flask import (
    Blueprint,
    g,
    json
)


api = Blueprint('api', __name__)


@api.route('/')
def ready():
    return json.jsonify({'ready': 'yes'})


@api.route('/categories')
def get_categories():
    result = {
        'error': '',
        'results': [],
    }
    cur = g.db.execute('select * from categories')
    for row in cur:
        result['results'].append({
            'slug': row[0],
            'category': row[1],
        })
    return json.jsonify(result)


@api.route('/category/<category>')
def get_category(category):
    result = {
        'error': '',
        'result': {},
    }
    row = g.db.execute('select * from categories where slug = ?',
                       (category,)).fetchone()
    if row is not None:
        result['result'] = {
            'slug': row[0],
            'category': row[1],
        }
    else:
        result['error'] = 'category not found'
    return json.jsonify(result)


@api.route('/category/<category>/topics')
def get_topics(category):
    result = {
        'error': '',
        'results': [],
    }
    category_exists = g.db.execute('select * from categories where slug = ?',
                                   (category,)).fetchone() is not None
    if not category_exists:
        result['error'] = 'category not found'
        return json.jsonify(result)
    cur = g.db.execute('''
        select
            topics.slug,
            topics.topic,
            topics.category,
            categories.category
        from topics
            join categories on topics.category = categories.slug
        where topics.category = ?''', (category,))
    for row in cur:
        result['results'].append({
            'slug': row[0],
            'topic': row[1],
            'category_slug': row[2],
            'category': row[3],
        })
    return json.jsonify(result)


@api.route('/category/<category>/topic/<topic>')
def get_topic(category, topic):
    result = {
        'error': '',
        'results': [],
    }
    topic_exists = g.db.execute(
        'select * from topics where slug = ? and category = ?',
        (topic, category)).fetchone() is not None
    if not topic_exists:
        result['error'] = 'topic not found'
        return json.jsonify(result)
    cur_topicexpertises = g.db.execute('''
        select
            topicexpertise.*,
            topics.topic,
            categories.category
        from topicexpertise
            join topics on topics.id = topicexpertise.topic
            join categories on categories.slug = topics.category
        where topics.slug = ? and topics.category = ?''',
        (topic, category))
    for row in cur_topicexpertises:
        expertise = g.db.execute('select * from expertise where id = ?',
                               (row[2],)).fetchone()
        expertise_result = {
            'expertise_id': row[2],
            'expertise': expertise[2],
            'content_warning': expertise[3],
            'expertise_topics': [],
            'topic_slug': topic,
            'topic': row[3],
            'category_slug': category,
            'category': row[4],
            'user': expertise[1],
        }
        topics = g.db.execute('''
            select
                topicexpertise.id,
                topics.slug,
                topics.topic,
                categories.slug,
                categories.category
            from topicexpertise
                join topics on topics.id = topicexpertise.topic
                join categories on categories.slug = topics.category
            where topicexpertise.expertise = ?''', (row[2],))
        for row in topics:
            topic_result = {
                'category_slug': row[3],
                'category': row[4],
                'topic_slug': row[1],
                'topic': row[2],
            }
            expertise_result['expertise_topics'].append(topic_result)
        result['results'].append(expertise_result)
    return json.jsonify(result)


@api.route('/users')
def get_users():
    result = {
        'error': '',
        'results': [],
    }
    cur = g.db.execute('select username from users')
    for row in cur:
        result['results'].append({
            'username': row[0],
        })
    return json.jsonify(result)


@api.route('/user/<user>')
def get_user(user):
    result = {
        'error': '',
        'results': []
    }
    user_exists = g.db.execute('select * from users where username = ?',
                               (user,)).fetchone() is not None
    if not user_exists:
        result['error'] = 'user not found'
        return json.jsonify(result)
    cur = g.db.execute('select * from expertise where user = ?',
                     (user,))
    for row in cur:
        expertise_result = {
            'expertise_id': row[0],
            'expertise': row[2],
            'content_warning': row[3] == 1,
            'expertise_topics': [],
            'user': row[1],
        }
        topics = g.db.execute('''
            select
                topicexpertise.id,
                topics.slug,
                topics.topic,
                categories.slug,
                categories.category
            from topicexpertise
                join topics on topics.id = topicexpertise.topic
                join categories on categories.slug = topics.category
            where topicexpertise.expertise = ?''', (row[0],))
        for row in topics:
            topic_result = {
                'category_slug': row[3],
                'category': row[4],
                'topic_slug': row[1],
                'topic': row[2],
            }
            expertise_result['expertise_topics'].append(topic_result)
        result['results'].append(expertise_result)
    return json.jsonify(result)
