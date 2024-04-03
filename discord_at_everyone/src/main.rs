use std::env;

fn main() {
    if env::args().len() != 2 {
        panic!("where args????");
    }
}
