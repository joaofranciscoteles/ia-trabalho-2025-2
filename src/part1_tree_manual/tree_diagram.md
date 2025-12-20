flowchart TD

start([Início]) --> q1{1. Você gosta de adrenalina?}

q1 -- Sim --> q10{10. Prefere ritmo acelerado?}
q1 -- Não --> q2{2. Gosta de filmes leves e engraçados?}

q10 -- Sim --> s_action[Ação]
q10 -- Não --> s_adventure1[Aventura]

q2 -- Sim --> s_comedy[Comédia]
q2 -- Não --> q4{4. Gosta de tensão/medo?}

q4 -- Sim --> s_horror[Terror]
q4 -- Não --> q3{3. Gosta de histórias emocionais e profundas?}

q3 -- Sim --> s_drama1[Drama]
q3 -- Não --> q5{5. Gosta de histórias românticas/afetivas?}

q5 -- Sim --> q7{7. Prefere finais felizes clichês?}
q5 -- Não --> q6{6. A história te leva para fora da realidade comum?}

q6 -- Sim --> q8{8. Tecnologia/futuro/espaço?}
q6 -- Não --> q9{9. Gosta de jornadas/viagens/descobertas?}

q7 -- Sim --> s_romcom[Comédia_Romântica]
q7 -- Não --> s_romdra[Romance_Dramático]

q8 -- Sim --> s_scifi[Ficção Científica]
q8 -- Não --> s_fantasy[Fantasia]

q9 -- Sim --> s_adventure2[Aventura]
q9 -- Não --> s_documentario[Documentário]
