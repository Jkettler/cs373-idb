def q1():
    return \
    '''SELECT
            name                                                                                  
        FROM
            idb_vote v 
        LEFT JOIN
            idb_senator s
            ON v.senator_id = s.id
        WHERE
            v.vote='ABS' '''

def q2():
    return \
    ''' SELECT
                name, S.NayCount AS NayCount          
            FROM
            ( 
                SELECT
                    senator_id, NayCount                                              
                FROM
                (
                    SELECT
                        senator_id,
                        COUNT(*) as NayCount                                                                                    
                    FROM
                        idb_vote                                                                                        
                    LEFT JOIN
                        idb_senator                                                                                                                                                                           
                            ON idb_vote.senator_id = idb_senator.id                                                                           
                    WHERE
                        idb_vote.vote = 'NAY'
                    GROUP BY
                        idb_vote.senator_id
                ) AS R
               
            ) AS S
            INNER JOIN idb_senator
                ON S.senator_id = idb_senator.id
            ORDER BY S.NayCount DESC
            LIMIT 1'''
def q3():
    return \
    '''     SELECT
                name, S.AuthorCount AS AuthorCount        
            FROM
            ( 
                SELECT
                    senator_id, AuthorCount                                              
                FROM
                (
                    SELECT
                        senator_id,
                        COUNT(*) as AuthorCount                                                                                    
                    FROM
                        idb_bill_authors                                                                                        
                    JOIN
                        idb_senator                                                                                                                                                                           
                            ON idb_bill_authors.senator_id = idb_senator.id
                    GROUP BY 
                        idb_bill_authors.senator_id
                ) AS R
               
            ) AS S
            INNER JOIN idb_senator
                ON S.senator_id = idb_senator.id
            ORDER BY S.AuthorCount DESC
            LIMIT 2'''
def q4():
    return \
    '''     SELECT
                name, S.CommitteeCount AS CommitteeCount          
            FROM
            ( 
                SELECT
                    senator_id, CommitteeCount                                             
                FROM
                (
                    SELECT
                        senator_id,
                        COUNT(*) as CommitteeCount                                                                                    
                    FROM
                        idb_committee_senators                                                                                        
                    JOIN
                        idb_senator                                                                                                                                                                           
                            ON idb_committee_senators.senator_id = idb_senator.id
                    GROUP BY 
                        idb_committee_senators.senator_id
                ) AS R
                WHERE R.CommitteeCount =
                (
                    SELECT
                        MAX(CommitteeCount) 
                    FROM
                    (
                        SELECT
                            COUNT(*) as CommitteeCount
                        FROM
                            idb_committee_senators
                        JOIN
                            idb_senator
                                ON idb_committee_senators.senator_id = idb_senator.id
                        GROUP BY
                            idb_committee_senators.senator_id
                    ) AS T
               )
            ) AS S
            INNER JOIN idb_senator
                ON S.senator_id = idb_senator.id
            ORDER BY S.CommitteeCount DESC'''
def q5():
    return \
    '''     SELECT
                name,
                T.date_proposed AS date_proposed,
                T.date_effective AS date_effective, 
                T.date_effective - T.date_proposed AS days_in_between
            FROM
                (
                    SELECT
                        name,
                        date_proposed,
                        date_effective,
                        date_effective - date_proposed AS Days_In_Between
                    FROM
                        (
                            SELECT
                                name,
                                date_proposed,
                                date_effective,
                                date_effective - date_proposed AS Days_In_Between
                            FROM
                                idb_bill
                            GROUP BY
                                idb_bill.id
                         ) AS R
                    WHERE
                        R.Days_In_Between = 
                    (
                        SELECT
                            MAX(DAYS_IN_BETWEEN)
                        FROM
                        (
                            SELECT
                                name,
                                date_proposed,
                                date_effective,
                                date_effective - date_proposed AS Days_In_Between
                            FROM
                                idb_bill
                            GROUP BY
                                idb_bill.id
                        ) AS S
                    )
                ) AS T       
                    
            ORDER BY
                Days_In_Between DESC '''