% Medical Diagnosis Expert System

% Facts: symptoms for each disease
disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(sore_throat),
    symptom(runny_nose).

disease(malaria) :-
    symptom(fever),
    symptom(chills),
    symptom(sweating),
    symptom(headache).

disease(typhoid) :-
    symptom(fever),
    symptom(abdominal_pain),
    symptom(loss_of_appetite),
    symptom(constipation).

disease(common_cold) :-
    symptom(runny_nose),
    symptom(sneezing),
    symptom(sore_throat).

% Rules to ask user for symptoms dynamically
ask(Question) :-
    write('Do you have '), write(Question), write('? (yes/no): '),
    read(Response),
    (Response == yes -> assert(symptom(Question));
     Response == no  -> fail).

start :-
    retractall(symptom(_)),  % Clear previous symptoms
    write('--- Medical Diagnosis System ---'), nl,
    (   (disease(D), write('You may have: '), write(D), nl, fail);
        write('Diagnosis complete.'), nl
    ).

% To run:
% ?- start.
