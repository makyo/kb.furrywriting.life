insert into users values (
    "user0expertise",
    ""
);
insert into users values (
    "user1expertise",
    ""
);
insert into users values (
    "user2expertise",
    ""
);

insert into categories values (
    "cat-empty",
    "empty category"
);
insert into categories values ("cat-one",
    "category with one topic"
);
insert into categories values ("cat-two",
    "category with two topics"
);

insert into topics values (
    "topic-empty",
    "empty topic",
    "cat-two"
);
insert into topics values (
    "topic-one",
    "topic with one expertise",
    "cat-two"
);
insert into topics values (
    "topic-two",
    "topic with two expertise",
    "cat-one"
);

insert into expertise (user, topic, expertise) values (
    "user1expertise",
    "topic-two",
    "Some expertise one"
);
insert into expertise (user, topic, expertise) values (
    "user2expertise",
    "topic-one",
    "Some expertise two"
);
insert into expertise (user, topic, expertise) values (
    "user2expertise",
    "topic-two",
    "Some expertise three"
);
