/**
 * Copyright (c) 2017-present, Facebook, Inc.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */

/**
 * React component for displaying lesson objectives
 */
import React from 'react';
import clsx from 'clsx';
import styles from './LessonObjectives.module.css';

const LessonObjectivesList = [
  {
    title: 'Understand Core Concepts',
    description: (
      <>
        Learn the fundamental principles of Physical AI and its application in humanoid robotics.
      </>
    ),
  },
  {
    title: 'Implement Technical Skills',
    description: (
      <>
        Develop practical skills in ROS 2, simulation environments, and AI integration.
      </>
    ),
  },
  {
    title: 'Apply Knowledge Practically',
    description: (
      <>
        Complete hands-on projects that integrate all course concepts into complete robotic systems.
      </>
    ),
  },
];

function LessonObjective({title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageLessonObjectives() {
  return (
    <section className={styles.objectives}>
      <div className="container">
        <div className="row">
          {LessonObjectivesList.map((props, idx) => (
            <LessonObjective key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}