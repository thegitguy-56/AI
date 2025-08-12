% --- Database of people ---
% Format: person(Name, DOB).
% DOB format: date(DD, MM, YYYY).

person(john, date(15, 5, 1995)).
person(mary, date(23, 8, 1998)).
person(alex, date(1, 1, 2000)).
person(sophia, date(12, 12, 1997)).
person(david, date(7, 3, 1993)).

% --- Rule to display all people ---
show_people :-
    person(Name, date(D, M, Y)),
    format("Name: ~w, DOB: ~w-~w-~w~n", [Name, D, M, Y]),
    fail.
show_people.

% --- Rule to find DOB by name ---
find_dob(Name) :-
    person(Name, date(D, M, Y)),
    format("DOB of ~w is ~w-~w-~w~n", [Name, D, M, Y]).

% --- Rule to find people born in a specific year ---
born_in_year(Year) :-
    person(Name, date(_, _, Year)),
    format("~w was born in ~w~n", [Name, Year]),
    fail.
born_in_year(_).