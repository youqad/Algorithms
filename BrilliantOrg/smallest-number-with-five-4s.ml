module IntSet = Set.Make(struct
                              type t = int * string
                              let compare t t' = let (x,y) = t and (x', y')=t'
                                in Pervasives.compare x x'
  end)

exception Not_allowed

let c = 4

let rec factorial n = if n = 0 then 1 else n * factorial (n - 1)


let bin_op = [((+), "+"); ((-), "-"); (( * ), "*"); ((fun n m -> if n mod m = 0 then n/m else raise Not_allowed), "/"); ((fun n m -> int_of_string((string_of_int n)^(string_of_int m))), ""); ((fun n m -> int_of_float ((float_of_int n)**(float_of_int m))), "^")]

let unary_op = [(factorial, "!"); ((fun n -> n), ""); ((fun n -> let m=truncate (sqrt (float n)) in if n=m*m then m else raise Not_allowed), "^(1/2)")]

let cartesian_two l =
  List.concat (List.map (fun e -> List.map (fun e' -> (e,e')) l) l)

let cartesian_three l =
  List.concat (List.concat (List.map (fun e -> List.map (fun e' -> List.map (fun e'' -> (e,e',e'')) l) l) l))

let cartesian_four l =
  List.concat (List.concat (List.concat (
      List.map (fun e ->
          List.map (fun e' ->
              List.map (fun e'' ->
                  List.map (fun e''' -> (e,e',e'',e'')) l) l) l) l)))

let all_possible_int () =
  List.fold_left (fun set ((b1, sb1), (b2, sb2), (b3, sb3)) ->
      List.fold_left (fun set' ((u1, su1), (u2, su2), (u3, su3), (u4, su4)) ->
          let new_set0 =
            try
              IntSet.add ((b3 (b2 (b1 (u1 c) (u2 c)) (u3 c)) (u4 c)), ("( (4"^su1^" "^sb1^" 4"^su2^") "^sb2^" 4"^su3^" ) "^sb3^" 4"^su4)) set'
            with _ -> set' in
          let new_set1 =
            try
              IntSet.add ((b3 (b1 (u1 c) (u2 c)) (b2 (u3 c) (u4 c))), ("(4"^su1^" "^sb1^" 4"^su2^") "^sb3^" (4"^su3^" "^sb2^" 4"^su4^")")) set'
            with _ -> set' in
          let new_set2 =
            try
              IntSet.add ((b2 (b1 (u1 c) (u2 c)) (u3 c)), ("(4"^su1^" "^sb1^" 4"^su2^") "^sb2^" 4"^su3)) new_set1
            with _ -> new_set1 in
          let new_set3 =
            try
              IntSet.add ((b1 (u1 c) (u2 c)), ("4"^su1^" "^sb1^" 4"^su2)) new_set2
          with _ -> new_set2 in
            new_set3)
        set (cartesian_four unary_op))
    IntSet.empty
    (cartesian_three bin_op)

let _ = IntSet.iter (fun (n, s) -> if n>=0 then Printf.printf "%d = %s \n" n s) (all_possible_int ());;

