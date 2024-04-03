use std::env;

use thirtyfour::prelude::*;

#[tokio::main]
async fn main() {
    println!("for grupz");
    let argv: Vec<_> = env::args().collect();
    let group_id: &str;

    if argv.len() < 2 { panic!("where args????"); }
    else { group_id = argv[1].as_str(); }

    let chromium_conf_path = env::var("ACPU_CHROMIUM_CONF_PATH").unwrap();
    let caps = DesiredCapabilities::chrome();
    let driver = WebDriver::new("http://localhost:8515", caps).await?;

    let url = format!("https://discord.com/channels/@me/{}", group_id);
    driver.goto(url).await;
}
