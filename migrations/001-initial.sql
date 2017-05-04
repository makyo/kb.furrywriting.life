create table if not exists users (
    username char(50) primary key,
    pass char(60)
);

create table if not exists categories (
    slug char(50) primary key,
    category text not null
);

create table if not exists topics (
    slug char(50) primary key,
    topic text not null,
    category char(50) not null,
    foreign key(category) references categories(slug)
);

create table if not exists expertise (
    id integer primary key autoincrement,
    user char(50),
    topic char(50),
    expertise text,
    foreign key(user) references users(id),
    foreign key(topic) references topics(id)
)
