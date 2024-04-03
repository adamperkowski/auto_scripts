use std::env;

fn main() {
    println!("for grupz");
    let argv: Vec<_> = env::args().collect();
    let group_id: &str;

    if argv.len() < 2 { panic!("where args????"); }
    else { group_id = argv[1].as_str(); }

    println!("https://discord.com/channels/@me/{}", group_id);
}
