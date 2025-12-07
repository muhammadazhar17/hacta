/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

import React from 'react';
import clsx from 'clsx';
import styles from './HomepageFeatures.module.css';
import Link from '@docusaurus/Link';

const FeatureList = [
  {
    title: 'Physical AI Concepts',
    Svg: require('@site/static/img/undraw_docusaurus_mountain.svg').default,
    description: (
      <>
        Learn the fundamental concepts of Physical AI - AI systems that interact 
        with and operate within the physical world, combining perception, 
        cognition, and action.
      </>
    ),
    link: '/docs/why-physical-ai-matters'
  },
  {
    title: 'ROS 2 Integration',
    Svg: require('@site/static/img/undraw_docusaurus_tree.svg').default,
    description: (
      <>
        Master Robot Operating System 2 (ROS 2) - the middleware that connects 
        all components of a robotic system, enabling communication between 
        different robot subsystems.
      </>
    ),
    link: '/docs/module-1-ros2-nervous-system/overview'
  },
  {
    title: 'Humanoid Robotics',
    Svg: require('@site/static/img/undraw_docusaurus_react.svg').default,
    description: (
      <>
        Explore humanoid robotics - robots with human-like form and capabilities, 
        designed to operate in human environments and interact with human tools.
      </>
    ),
    link: '/docs/module-4-vision-language-action/overview'
  },
];

function Feature({Svg, title, description, link}) {
  return (
    <div className="col col--4">
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <h3><Link to={link}>{title}</Link></h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}