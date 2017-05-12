create table if not exists users (
    username char(50) primary key
);

create table if not exists categories (
    slug char(50) primary key,
    category text not null
);

create table if not exists topics (
    id integer primary key autoincrement,
    slug char(50) not null,
    topic text not null,
    category char(50) not null,
    foreign key(category) references categories(slug)
);

create table if not exists topicexpertise (
    id integer primary key autoincrement,
    topic integer not null,
    expertise integer not null,
    foreign key(topic) references topics(id),
    foreign key(expertise) references expertises(id)
);

create table if not exists expertise (
    id integer primary key autoincrement,
    user char(50),
    expertise text,
    content_warning boolean,
    foreign key(user) references users(username)
);
