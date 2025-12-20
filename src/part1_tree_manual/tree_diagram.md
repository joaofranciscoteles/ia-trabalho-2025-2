flowchart TD
start([Início]) --> q1{1. Quer Adrenalina/Tensão?}

    
q1 -- Sim --> q2{2. Quer sentir medo?}
q2 -- Sim --> R_Terror[Terror]
q2 -- Não --> q3{3. Gosta de explosões/lutas?}
    
q3 -- Sim --> R_Acao[Ação]
q3 -- Não --> q4{4. Prefere mistérios/crimes?}
    
q4 -- Sim --> R_Suspense[Suspense/Policial]
q4 -- Não --> q5{5. Envolve futuro/espaço?}
    
q5 -- Sim --> R_SciFi[Ficção Científica]
q5 -- Não --> R_Aventura[Aventura]

   
q1 -- Não --> q6{6. Quer dar risada?}
q6 -- Sim --> R_Comedia[Comédia]
q6 -- Não --> q7{7. Quer se emocionar/chorar?}
    
q7 -- Sim --> R_Drama[Drama]
q7 -- Não --> q8{8. Foco em romance?}
    
q8 -- Sim --> q9{9. Prefere final feliz/leve?}
q9 -- Sim --> R_ComRom[Comédia Romântica]
q9 -- Não --> R_RomDrama[Romance Dramático]
    
q8 -- Não --> q10{10. Gosta de magia/irreal?}
q10 -- Sim --> R_Fantasia[Fantasia]
q10 -- Não --> R_Doc[Documentário/Bio]