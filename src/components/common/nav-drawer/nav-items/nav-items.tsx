import React from "react";
import { NavItem } from "../nav-item";

import HomeIcon from "@mui/icons-material/Home";
import HttpIcon from "@mui/icons-material/Http";
import TerminalIcon from "@mui/icons-material/Terminal";
import BarChart from "@mui/icons-material/BarChart";
import AutoAwesomeIcon from "@mui/icons-material/AutoAwesome";
import { List } from "@mui/material";
import { Schedule, VideoFile } from "@mui/icons-material";

const items = [
  {
    icon: <HomeIcon />,
    text: "Home",
    href: "/",
  },
  {
    icon: <HttpIcon />,
    text: "Jobs",
    href: "/jobs",
  },
  {
    icon: <AutoAwesomeIcon />,
    text: "Chat",
    href: "/chat",
  },
  {
    icon: <BarChart />,
    text: "Statistics",
    href: "/statistics",
  },
  {
    icon: <Schedule />,
    text: "Cron Jobs",
    href: "/cron-jobs",
  },
  {
    icon: <VideoFile />,
    text: "Recordings",
    href: "/recordings",
  },
];

export const NavItems = () => {
  return (
    <List>
      {items.map((item) => (
        <NavItem key={item.href} {...item} />
      ))}
    </List>
  );
};
